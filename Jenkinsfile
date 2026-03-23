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
                    # compile java file in root folder
                    javac -d build Javafile.java
                    echo "Running Java Program..."
                    java -cp build Javafile
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                echo "Running Python script..."
                sh '''
                    python3 test.py
                '''
            }
        }

        stage('Validate HTML') {
            steps {
                echo "Validating HTML..."
                sh '''
                    # tidy works on most systems
                    tidy -errors index.html || true
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
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
