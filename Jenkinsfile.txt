pipeline{
	agent any
	stages{
		stage('Build'){
			cd /home/remlab/Desktop/demo/python
			python example.py
		}
	}
}