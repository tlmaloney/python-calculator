pipeline {

    agent {
        docker {
            image 'node'
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
		
        stage('Test') {
			{
            steps {
                echo 'Testing...'
                sh 'pytest --junit-xml=test_results.xml'
            }
        }
    }
}
