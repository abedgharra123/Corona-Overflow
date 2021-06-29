pipeline {
    agent {
        docker {
            image 'python:3.9.2'

        }
    }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m pip install -r requirements.txt"
                }
            }
        }
        stage('Test'){
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python manage.py test' 

                }
            }
        }
        stage('coverage') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m coverage run manage.py test"
                    sh "python -m coverage report"

                }
            }
        }
        stage('pylint') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("blog"){
                        sh "python -m pylint views.py"
                        sh "python -m pylint admin.py"
                        sh "python -m pylint apps.py"
                        sh "python -m pylint models.py"
                        sh "python -m pylint tests.py"
                        

                    }
                }
            }
        }
        
    }
}
