pipeline {
    agent any

    environment{
        venv_dir= venv
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                // Clone Repository
                script {
                    echo 'Cloning GitHub Repository...'
            
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github_jenkins_token', url: 'https://github.com/chirag1dev/ml_pipeline.git']])
                }
            }
        }
        stage('Clone creating virtual environment') {
            steps {
                // Clone Repository
                script {
                    echo 'set up virtual environment...'
                    sh '''python -m venv ${venv_dir}
                    source ${venv_dir}/bin/activate
                    pip install --upgrade pip
                    pip install -e .'''
                }
            }
        }


        stage('Lint Code') {
            steps {
                // Lint code
                script {
                    echo 'Linting Python Code...'
                    set -e
                    . ${VENV_DIR}/bin/activate
                    sh ''' python3 -m pip install --break-system-packages -r requirements.txt"
                    pylint app.py train.py --output=pylint-report.txt --exit-zero"
                    flake8 app.py train.py --ignore=E501,E302 --output-file=flake8-report.txt"
                    black app.py train.py '''
                }
            }
        }
    }
}

        