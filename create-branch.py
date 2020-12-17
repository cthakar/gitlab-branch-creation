import sys
import gitlab
import os

gl = gitlab.Gitlab('https://gitlab.com/', private_token=os.environ.get("token"))        
gl.auth()

class CreateBranch():
    
    def __call__(self):
        urls = self._read_from_file()
        self._auth_gitlab(urls)

    def _auth_gitlab(self, urls):

        for url in urls:
            pro_path = (url.split('/',3)[3])
            #print(pro_path)
            project = gl.projects.get(pro_path)
            #print(project.id)
            project = gl.projects.get(project.id)
            # branch = project.branches.create({'branch': 'feature2',
            #                                   'ref': 'master'})
            branch = project.branches.create({'branch': sys.argv[2],
                                              'ref': sys.argv[1]})
            print("Successfully created branches")
            

    def _read_from_file(self):
        list = []
        with open('repo.txt','r') as repo_list:
            for apps in repo_list.readlines():
                list.append(apps.strip())
                #print(apps.strip())

        return list

if __name__ == "__main__":
    cb = CreateBranch()
    cb()
