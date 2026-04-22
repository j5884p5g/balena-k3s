import yaml

def check_all_jobs(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    jobs = data.get('jobs', {})
    dependencies = {}
    for job_name, job_data in jobs.items():
        needs = job_data.get('needs', [])
        if isinstance(needs, str):
            needs = [needs]
        dependencies[job_name] = needs

    all_job_names = set(jobs.keys())
    
    def get_all_ancestors(job_name):
        ancestors = set()
        for dep in dependencies.get(job_name, []):
            ancestors.add(dep)
            ancestors.update(get_all_ancestors(dep))
        return ancestors

    for job_name in all_job_names:
        if job_name == 'event_types':
            continue
        ancestors = get_all_ancestors(job_name)
        if 'event_types' not in ancestors:
            print(f"Job {job_name} DOES NOT depend on event_types!")
            print(f"  Direct needs: {dependencies[job_name]}")
            print(f"  All ancestors: {ancestors}")
            print("-" * 20)

if __name__ == "__main__":
    check_all_jobs('/home/nils/pwnhunter/attack-artifacts/20260415T170932Z/balena-io-experimental__balena-k3s/risks/risk-011-pwnrequestresult/workspace/flowzone_reusable.yml')
