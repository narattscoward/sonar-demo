pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                sh 'pytest --cov=. --cov-report=xml'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    script {
                        def scannerHome = tool 'SonarScanner'
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                              -Dsonar.projectKey=sonar-demo \
                              -Dsonar.sources=. \
                              -Dsonar.python.coverage.reportPaths=coverage.xml \
                              -Dsonar.host.url=http://sonarqube:9000 \
                              -Dsonar.token=$SONAR_AUTH_TOKEN
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}