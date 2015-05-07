from project_module import project_object, image_object, link_object, challenge_object

p = project_object('ScramBuildEggs', 'ScramBuildEggs')
p.domain = 'http://www.aidansean.com/'
p.path = ''
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'ScramBuildEggs'
p.mathjax = True
p.introduction = 'This project parses a build log and gives more untuitive output.'
p.overview = '''This is a script that parses the build log created by the CMSSW command "scram build" (hence the name!)  It takes the output, wraps it to a more readable width, splits errors by type and colours them, and also gives more useful output.  It's not complete yet, but it is already rather useful.'''
