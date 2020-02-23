pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('Test') {
            steps {
                sh 'pipenv run pytest -vv'
            }
        }
    }
}