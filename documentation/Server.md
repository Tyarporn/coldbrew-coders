Server Documentation

Details
- AWS EC2 t2.micro (Hardware)
- Amazon Linux OS (Software)

Note:
The server is by default off for cost savings. It can be turned on manually or programatically by Github Actions

To run:
- Log into Coldbrew AWS account 
- Navigate to EC2 console
- Check coldbrew-api
- Click Instance State -> Start instance
- Either SSH or use EC2 browser to access server terminal
- run 
    export PATH=/home/ec2-user/.local/bin:$PATH
    export PYTHONPATH=/home/ec2-user/coldbrew-coders/server:$PYTHONPATH
    export PYTHONPATH=/home/ec2-user/coldbrew-coders/:$PYTHONPATH
    export PYTHONPATH=/home/ec2-user/coldbrew-coders/db:$PYTHONPATH

    cd ..
    cd ..
    cd home/ec2-user/coldbrew-coders/