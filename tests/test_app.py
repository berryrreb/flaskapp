import os
import unittest
import tempfile
import app as flask_app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Crear un archivo temporal para la base de datos de prueba
        self.db_fd, flask_app.DATABASE = tempfile.mkstemp()
        flask_app.app.config['TESTING'] = True
        self.app = flask_app.app.test_client()
        
        # Inicializar la base de datos de prueba
        with flask_app.app.app_context():
            flask_app.init_db()

    def tearDown(self):
        # Cerrar y eliminar la base de datos temporal
        os.close(self.db_fd)
        os.unlink(flask_app.DATABASE)

    def test_empty_db(self):
        """Verifica que la página principal cargue y empiece vacía."""
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'prompt-grid', rv.data or b'')
        self.assertNotIn(b'prompt-card', rv.data or b'')

    def test_add_prompt(self):
        """Prueba la adición de un nuevo prompt."""
        rv = self.app.post('/add', data=dict(
            title='Test Title',
            content='Test Content',
            category='Development'
        ), follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Test Title', rv.data)
        self.assertIn(b'Development', rv.data)

    def test_view_prompt(self):
        """Prueba ver los detalles de un prompt."""
        # Agregar uno primero
        self.app.post('/add', data=dict(
            title='Detail Title',
            content='This is a detailed prompt content.',
            category='Testing'
        ))
        
        # Obtener los detalles del primer prompt (id=1)
        rv = self.app.get('/prompt/1')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Detail Title', rv.data)
        self.assertIn(b'This is a detailed prompt content.', rv.data)

    def test_view_prompt_not_found(self):
        """Prueba que un prompt inexistente devuelva 404."""
        rv = self.app.get('/prompt/999')
        self.assertEqual(rv.status_code, 404)

    def test_edit_prompt(self):
        """Prueba la edición de un prompt existente."""
        self.app.post('/add', data=dict(
            title='Original Title',
            content='Original Content',
            category='Original Category'
        ))
        
        rv = self.app.post('/edit/1', data=dict(
            title='Updated Title',
            content='Updated Content',
            category='Updated Category'
        ), follow_redirects=True)
        
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Updated Title', rv.data)
        self.assertIn(b'Updated Category', rv.data)
        self.assertNotIn(b'Original Title', rv.data)

    def test_delete_prompt(self):
        """Prueba la eliminación de un prompt."""
        self.app.post('/add', data=dict(
            title='Delete Me',
            content='Some content',
            category='Misc'
        ))
        
        # Eliminarlo usando POST
        rv = self.app.post('/delete/1', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertNotIn(b'Delete Me', rv.data)

    def test_search_prompt(self):
        """Prueba la funcionalidad de búsqueda."""
        self.app.post('/add', data=dict(
            title='UniqueSearchTitle',
            content='Content here',
            category='Work'
        ))
        self.app.post('/add', data=dict(
            title='Another Normal Title',
            content='Content here',
            category='Home'
        ))
        
        # Buscar por título único
        rv = self.app.get('/?q=UniqueSearchTitle')
        self.assertIn(b'UniqueSearchTitle', rv.data)
        self.assertNotIn(b'Another Normal Title', rv.data)

if __name__ == '__main__':
    unittest.main()
