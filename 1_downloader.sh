#$ -cwd -V
#$ -l h_rt=2:0:0
#$ -l h_vmem=4G
#$ -P omics

# Number of tasks = 22
#$ -t 1-22
#$ -tc 5
 
vid_id=`sed -n -e "$SGE_TASK_ID p" youtube.txt`

python 1_downloader.py --youtubeid $vid_id --output $vid_id.json


 

