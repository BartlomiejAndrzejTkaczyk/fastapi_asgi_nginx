import os
import subprocess
import sys


def copy_files_to_docker(container_id, source_dir):
    for root, dirs, files in os.walk(source_dir):
        # Exclude venv and .git directories
        if 'venv' in dirs:
            dirs.remove('venv')
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, source_dir)
            dest_dir = os.path.join('/app', os.path.dirname(relative_path)).replace("\\",
                                                                                    "/")  # Ensure UNIX-style paths
            dest_path = os.path.join('/app', relative_path).replace("\\", "/")

            # Create directory in the container if it doesn't exist
            subprocess.run(['docker', 'exec', container_id, 'mkdir', '-p', dest_dir])

            subprocess.run(['docker', 'cp', file_path, f'{container_id}:{dest_path}'])
            print('#', end='')

    print("\nAll files copied successfully.")


def get_container_id(image_name):
    try:
        result = subprocess.run(
            ['docker', 'ps', '--filter', f'ancestor={image_name}', '--format', '{{.ID}}'],
            capture_output=True,
            text=True,
            check=True
        )

        container_id = result.stdout.strip()

        if container_id:
            print(f"Container ID for image '{image_name}': {container_id}")
        else:
            print(f"No running container found for image '{image_name}'")

        return container_id

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while getting container ID: {e}")
        return None

if __name__ == '__main__':
    container_id = get_container_id('fastapi_asgi_nginx-fastapi')
    source_dir = os.path.dirname(os.getcwd())
    if container_id == '':
        print('Error: Unable to get current working directory.')
    else:
        print('Copy from: ', source_dir)
        copy_files_to_docker(container_id, source_dir)

