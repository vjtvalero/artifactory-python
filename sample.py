from artifactory.repositories import Repositories
import os
from dotenv import load_dotenv
load_dotenv()

# instantiate class
instance = Repositories(
    os.getenv('ARTIFACTORY_URL'), os.getenv('ARTIFACTORY_USERNAME'), os.getenv('ARTIFACTORY_PASSWORD'))

# get all repos
print(instance.get_all())


# create repo
new_repo = {
    "rclass": "local"
}
response = instance.create_repo('libs-release-local', new_repo)
print(response)
