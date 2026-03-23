pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Pulling source code..."
                checkout scm
            }
        }

        stage('Java Build & Run') {
            steps {
                echo "Compiling Java code..."
                sh '''
                    mkdir -p build
                    javac -d build src/java/Javafile.java
                    echo "Running Java Program..."
                    java -cp build Hello
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                echo "Executing Python script..."
                sh '''
                    python3 scripts/python.py
                '''
            }
        }

        stage('Validate HTML File') {
            steps {
                echo "Checking HTML file..."
                sh '''
                    # Option 1: Using tidy (common)
                    tidy -errors src/html/index.html || true

                    # Option 2: Using htmlhint (if installed)
                    # htmlhint src/html/Htmlfile.html
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo "Archiving build outputs..."
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
