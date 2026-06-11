pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat 'flake8 .'
            }
        }

        stage('Unit Test') {
            steps {
                bat 'pytest'
            }
        }
    }
}