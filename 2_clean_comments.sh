#$ -cwd -V
#$ -l h_rt=2:0:0
#$ -l h_vmem=4G
#$ -P omics

# Number of tasks = 22
#$ -t 1-22
#$ -tc 5
 
text_id=`sed -n -e "$SGE_TASK_ID p" textfiles.txt`

python 2_clean_comments.py $text_id



 

