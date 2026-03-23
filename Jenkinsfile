pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo "Pulling source code from branch1..."
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'origin/branch1']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/jibishwaran07/DemoTest.git'
                    ]]
                ])
            }
        }

        stage('Java Build & Run') {
            steps {
                echo "Compiling Java code..."
                sh '''
                    mkdir -p build

                    # Compile Javafile.java from root
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
                    python3 python.py
                '''
            }
        }

        stage('Validate HTML File') {
            steps {
                echo "Validating HTML..."
                sh '''
                    # Validate Htmlfile.html
                    tidy -errors Htmlfile.html || true
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo "Archiving build output..."
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
