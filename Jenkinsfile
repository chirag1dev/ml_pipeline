pipeline {
    agent any
    environment {
        #DOCKERHUB_CREDENTIAL_ID = 'mlops-jenkins-dockerhub-token'
        #DOCKERHUB_REGISTRY = 'https://registry.hub.docker.com'
        #DOCKERHUB_REPOSITORY = 'iquantc/mlops-proj-01'
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Clone Repository
                script {
                    echo 'Cloning GitHub Repository...'
                    ##checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-git-token', url: 'https://github.com/iQuantC/MLOps01.git']])#
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github_jenkins_token', url: 'https://github.com/chirag1dev/ml_pipeline.git']])
                }
            }
        }
        stage('Lint Code') {
            steps {
                // Lint code
                script {
                    echo 'Linting Python Code...'
                    sh "python -m pip install --break-system-packages -r requirements.txt"
                    sh "pylint app.py train.py --output=pylint-report.txt --exit-zero"
                    sh "flake8 app.py train.py --ignore=E501,E302 --output-file=flake8-report.txt"
                    sh "black app.py train.py"
                }
            }
        }
    }
}
        