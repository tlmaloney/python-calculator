pipeline {
    stages {
         agent {
                docker {
                    image 'python:3-slim' 
                }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'pytest --junit-xml=test_results.xml'
            }
        }
    }
}
