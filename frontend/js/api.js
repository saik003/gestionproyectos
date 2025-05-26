// API Client para comunicación con el backend
const API_URL = 'http://localhost:5001/api';

const ApiClient = {
    // Tareas
    async getTasks() {
        try {
            const response = await fetch(`${API_URL}/tasks/`);
            if (!response.ok) throw new Error('Error al obtener tareas');
            return await response.json();
        } catch (error) {
            console.error('Error en getTasks:', error);
            return [];
        }
    },
    
    async getTask(id) {
        try {
            const response = await fetch(`${API_URL}/tasks/${id}`);
            if (!response.ok) throw new Error(`Error al obtener tarea ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en getTask:', error);
            return null;
        }
    },
    
    async createTask(taskData) {
        try {
            console.log('Enviando datos de tarea al servidor:', taskData);
            const response = await fetch(`${API_URL}/tasks/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(taskData)
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                console.error('Respuesta del servidor:', errorText);
                throw new Error(`Error al crear tarea: ${response.status} ${response.statusText}. ${errorText}`);
            }
            
            const data = await response.json();
            console.log('Respuesta exitosa del servidor:', data);
            return data;
        } catch (error) {
            console.error('Error detallado en createTask:', error);
            alert(`Error al guardar la tarea: ${error.message}`);
            return null;
        }
    },
    
    async updateTask(id, taskData) {
        try {
            const response = await fetch(`${API_URL}/tasks/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(taskData)
            });
            if (!response.ok) throw new Error(`Error al actualizar tarea ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en updateTask:', error);
            return null;
        }
    },
    
    async deleteTask(id) {
        try {
            const response = await fetch(`${API_URL}/tasks/${id}`, {
                method: 'DELETE'
            });
            if (!response.ok) throw new Error(`Error al eliminar tarea ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en deleteTask:', error);
            return null;
        }
    },
    
    async updateTaskStatus(id, status) {
        try {
            const response = await fetch(`${API_URL}/tasks/${id}/status`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status })
            });
            if (!response.ok) throw new Error(`Error al actualizar estado de tarea ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en updateTaskStatus:', error);
            return null;
        }
    },
    
    // Usuarios
    async getUsers() {
        try {
            const response = await fetch(`${API_URL}/users/`);
            if (!response.ok) throw new Error('Error al obtener usuarios');
            return await response.json();
        } catch (error) {
            console.error('Error en getUsers:', error);
            return [];
        }
    },
    
    async getUser(id) {
        try {
            const response = await fetch(`${API_URL}/users/${id}`);
            if (!response.ok) throw new Error(`Error al obtener usuario ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en getUser:', error);
            return null;
        }
    },
    
    async createUser(userData) {
        try {
            const response = await fetch(`${API_URL}/users/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            });
            if (!response.ok) throw new Error('Error al crear usuario');
            return await response.json();
        } catch (error) {
            console.error('Error en createUser:', error);
            return null;
        }
    },
    
    async updateUser(id, userData) {
        try {
            const response = await fetch(`${API_URL}/users/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            });
            if (!response.ok) throw new Error(`Error al actualizar usuario ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en updateUser:', error);
            return null;
        }
    },
    
    async deleteUser(id) {
        try {
            const response = await fetch(`${API_URL}/users/${id}`, {
                method: 'DELETE'
            });
            if (!response.ok) throw new Error(`Error al eliminar usuario ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en deleteUser:', error);
            return null;
        }
    },
    
    // Proyectos
    async getProjects() {
        try {
            const response = await fetch(`${API_URL}/projects/`);
            if (!response.ok) throw new Error('Error al obtener proyectos');
            return await response.json();
        } catch (error) {
            console.error('Error en getProjects:', error);
            return [];
        }
    },
    
    async getProject(id) {
        try {
            const response = await fetch(`${API_URL}/projects/${id}`);
            if (!response.ok) throw new Error(`Error al obtener proyecto ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en getProject:', error);
            return null;
        }
    },
    
    async createProject(projectData) {
        try {
            const response = await fetch(`${API_URL}/projects/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(projectData)
            });
            if (!response.ok) throw new Error('Error al crear proyecto');
            return await response.json();
        } catch (error) {
            console.error('Error en createProject:', error);
            return null;
        }
    },
    
    async updateProject(id, projectData) {
        try {
            const response = await fetch(`${API_URL}/projects/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(projectData)
            });
            if (!response.ok) throw new Error(`Error al actualizar proyecto ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en updateProject:', error);
            return null;
        }
    },
    
    async deleteProject(id) {
        try {
            const response = await fetch(`${API_URL}/projects/${id}`, {
                method: 'DELETE'
            });
            if (!response.ok) throw new Error(`Error al eliminar proyecto ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en deleteProject:', error);
            return null;
        }
    },
    
    // Registros Diarios
    async getDailyRecords() {
        try {
            debugger;
            const response = await fetch(`${API_URL}/daily-records/`);
            if (!response.ok) throw new Error('Error al obtener registros diarios');
            return await response.json();
        } catch (error) {
            console.error('Error en getDailyRecords:', error);
            return [];
        }
    },
    
    async getDailyRecordsByTask(taskId) {
        try {
            const response = await fetch(`${API_URL}/daily-records/task/${taskId}`);
            if (!response.ok) throw new Error(`Error al obtener registros de tarea ${taskId}`);
            return await response.json();
        } catch (error) {
            console.error('Error en getDailyRecordsByTask:', error);
            return [];
        }
    },
    
    async getDailyRecordsByUser(userId) {
        try {
            const response = await fetch(`${API_URL}/daily-records/user/${userId}`);
            if (!response.ok) throw new Error(`Error al obtener registros de usuario ${userId}`);
            return await response.json();
        } catch (error) {
            console.error('Error en getDailyRecordsByUser:', error);
            return [];
        }
    },
    
    async createDailyRecord(recordData) {
        try {
            const response = await fetch(`${API_URL}/daily-records/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(recordData)
            });
            if (!response.ok) throw new Error('Error al crear registro diario');
            return await response.json();
        } catch (error) {
            console.error('Error en createDailyRecord:', error);
            return null;
        }
    },
    
    async updateDailyRecord(id, recordData) {
        try {
            const response = await fetch(`${API_URL}/daily-records/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(recordData)
            });
            if (!response.ok) throw new Error(`Error al actualizar registro diario ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en updateDailyRecord:', error);
            return null;
        }
    },
    
    async deleteDailyRecord(id) {
        try {
            const response = await fetch(`${API_URL}/daily-records/${id}`, {
                method: 'DELETE'
            });
            if (!response.ok) throw new Error(`Error al eliminar registro diario ${id}`);
            return await response.json();
        } catch (error) {
            console.error('Error en deleteDailyRecord:', error);
            return null;
        }
    }
};
