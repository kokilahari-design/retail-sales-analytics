pipeline {
  stages {

    stage('Test') {
      steps {
        sh 'pytest'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t retail-api .'
      }
    }

    stage('Push') {
      steps {
        sh 'docker push retail-api'
      }
    }

    stage('Deploy') {
      steps {
        sh 'kubectl apply -f k8s/deployment.yaml'
      }
    }
  }
}
