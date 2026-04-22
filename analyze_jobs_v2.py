import yaml

def analyze_jobs(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    jobs = data.get('jobs', {})
    
    dependencies = {}
    for job_name, job_data in jobs.items():
        needs = job_data.get('needs', [])
        if isinstance(needs, str):
            needs = [needs]
        dependencies[job_name] = needs

    print("Jobs not directly needing event_types:")
    for job_name, needs in dependencies.items():
        if job_name != 'event_types' and 'event_types' not in needs:
            print(f"  - {job_name} (needs: {needs})")

if __name__ == "__main__":
    analyze_jobs('/home/nils/pwnhunter/attack-artifacts/20260415T170932Z/balena-io-experimental__balena-k3s/risks/risk-011-pwnrequestresult/workspace/flowzone_reusable.yml')
