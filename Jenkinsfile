pipeline {
    agent any

    environment {
        APP_NAME = "DemoApp"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Pulling code from GitHub..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the application..."
                sh 'echo "Build complete!"'
            }
        }

        stage('Unit Tests') {
            steps {
                echo "Running tests..."
                sh 'echo "All tests passed!"'
            }
        }

        stage('Package') {
            steps {
                echo "Packaging the application..."
                sh 'echo "Packaging done!"'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to server..."
                sh 'echo "Deployment successful!"'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
