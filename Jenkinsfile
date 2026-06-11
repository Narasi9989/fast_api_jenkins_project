pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
               bat 'pip install -r requirements.txt'
            }
        }

        stage('Code Quality Check') {
            steps {
                bat 'venv\\Scripts\\flake8 .'
            }
        }

        stage('Unit Testing') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage completed successfully.'
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }

        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}