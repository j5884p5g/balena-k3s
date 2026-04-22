import yaml

def analyze_jobs(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    jobs = data.get('jobs', {})
    
    # Map dependencies
    dependencies = {}
    for job_name, job_data in jobs.items():
        needs = job_data.get('needs', [])
        if isinstance(needs, str):
            needs = [needs]
        dependencies[job_name] = needs

    print(f"Total jobs: {len(jobs)}")
    
    roots = [job for job, deps in dependencies.items() if not deps]
    print(f"Roots: {roots}")

    # Function to check if a job depends on event_types
    memo = {}
    def depends_on_event_types(job_name):
        if job_name == 'event_types':
            return True
        if job_name in memo:
            return memo[job_name]
        
        for dep in dependencies.get(job_name, []):
            if depends_on_event_types(dep):
                memo[job_name] = True
                return True
        
        memo[job_name] = False
        return False

    independent_jobs = []
    for job_name in jobs:
        if job_name == 'event_types':
            continue
        if not depends_on_event_types(job_name):
            independent_jobs.append(job_name)

    print(f"Independent jobs (not depending on event_types): {independent_jobs}")

    for job_name in independent_jobs:
        print(f"Job: {job_name}")
        job_data = jobs[job_name]
        steps = job_data.get('steps', [])
        print("Steps:")
        for step in steps:
            name = step.get('name', step.get('uses', 'unnamed'))
            print(f"  - {name}")
        print("-" * 20)

if __name__ == "__main__":
    analyze_jobs('/home/nils/pwnhunter/attack-artifacts/20260415T170932Z/balena-io-experimental__balena-k3s/risks/risk-011-pwnrequestresult/workspace/flowzone_reusable.yml')
