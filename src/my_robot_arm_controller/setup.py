from setuptools import find_packages, setup

package_name = 'my_robot_arm_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adarsh-kumar',
    maintainer_email='adarsh754103@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talkernode = my_robot_arm_controller.talker_node:main',
            'listenernode = my_robot_arm_controller.listener_node:main'
        ],
    },
)
