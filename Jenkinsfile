pipeline {
    agent any

    stages {

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        ${tool "SonarScanner"}/bin/sonar-scanner \
                        -Dsonar.projectKey=sonar-demo \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000
                    '''
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