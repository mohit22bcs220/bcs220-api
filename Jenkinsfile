pipeline {
    agent any

    environment {
        IMAGE_NAME = "scoobydou/bcs220-api:latest"
        CONTAINER_NAME = "ml_test_container"
        PORT = "8000"
    }

    stages {

        stage('Pull Image') {
            steps {
                sh "docker pull ${IMAGE_NAME}"
            }
        }

        stage('Run Container') {
            steps {
                sh """
                docker run -d --network jenkins-net \
                --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }

        stage('Wait for Service') {
            steps {
                sleep 15
            }
        }

        stage('Valid Request Test') {
            steps {
                script {
                    def status = sh(
                        script: 'curl -s -o response.json -w "%{http_code}" -X POST http://ml_test_container:8000/predict -H "Content-Type: application/json" -d @tests/valid.json',
                        returnStdout: true
                    ).trim()

                    if (status != "200") {
                        error("Valid request failed!")
                    }
                }
            }
        }

        stage('Invalid Request Test') {
            steps {
                script {
                    def invalidStatus = sh(
                        script: 'curl -s -o invalid.json -w "%{http_code}" -X POST http://ml_test_container:8000/predict -H "Content-Type: application/json" -d @tests/invalid.json',
                        returnStdout: true
                    ).trim()

                    if (invalidStatus != "422") {
                        error("Invalid request test failed!")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                sh """
                docker stop ${CONTAINER_NAME}
                docker rm ${CONTAINER_NAME}
                """
            }
        }
    }
}