pipeline {
  agent any

  environment {
    FOO = "PIPELINE"
  }

  stages {
    stage("local") {
      environment {
        BAR = "STAGE"
      }
      steps {
        sh 'python scripts/transform.py'
      }
    }
  }
}
