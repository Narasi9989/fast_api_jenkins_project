pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
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
                bat 'echo Build stage completed successfully.'
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