pipeline {
    agent {
        {
            dockerfile true
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
