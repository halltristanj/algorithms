pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'sureshkvl/pytester'
                }
            }
            steps {
                sh 'py.test -vv --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}