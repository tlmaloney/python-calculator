pipeline {
    stages {
        agent {
            docker {
                image 'python:3-slim' 
            }
        }
        
        stage("test PythonEnv") {

            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest tests'
            }
        }
    }
}
