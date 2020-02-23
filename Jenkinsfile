pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'grihabor/pytest:python3.6-alpine'
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