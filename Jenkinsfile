stage('Python pytest Tests') {
	dir('tests') {
		sh 'virtualenv -p /usr/bin/python3 venv'
		sh 'source venv/bin/activate && pytest --junit-xml=test_results.xml test || true'
		junit keepLongStdio: true, allowEmptyResults: true, testResults: 'test_results.xml'
	}
}
