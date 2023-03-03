pipeline{
	agent any
	stages{
		stage('Build'){
			steps{
				sh''' cd /var/lib/jenkins/workspace
				echo "hello world"
				pwd'''
				sh'env | sort'
			}
		}
	}
}






