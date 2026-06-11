pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Narasi9989/fast_api_jenkins_project'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Code Quality Check') {
            steps {
                bat 'venv\\Scripts\\activate && flake8 .'
            }
        }

        stage('Unit Testing') {
            steps {
                bat 'venv\\Scripts\\activate && pytest'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Building application...'
                bat 'python setup.py sdist'
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