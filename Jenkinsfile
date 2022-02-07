pipeline {
    agent {
        docker {
            image 'python:3-slim' 
        }
    }
    stages {
        stage("test") {
            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest tests'
            }
        }
    }
}
