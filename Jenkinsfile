pipeline {
    agent {
        docker {
            image 'python:3-slim' 
        }
    }
    stages {
        stage("test") {

            steps {
                sh 'pip install pytest'
                sh 'pytest tests'
            }
        }
    }
}
