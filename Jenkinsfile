pipeline {
    stages {
        agent {
            docker {
                image 'python:3-slim' 
            }
        }
        
        stage("test") {

            steps {
                sh 'pip install pytest'
                sh 'pytest tests'
            }
        }
    }
}
