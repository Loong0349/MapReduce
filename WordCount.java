package wordcount;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static void main(String[] args) throws Exception {
        // Create a Hadoop configuration object to store configuration parameters
        Configuration conf = new Configuration();
        // Create a new MapReduce job instance and give it a name ("Word Count")
        Job job = Job.getInstance(conf, "Word Count");

        // Specify the main class (WordCount) for the job JAR file
        job.setJarByClass(WordCount.class);
        // Set the Mapper class to be used for the Word Count job
        job.setMapperClass(WCMapper.class);
        // Set the Reducer class to be used for the Word Count job
        job.setReducerClass(WCReducer.class);

        // Specify the output key class for the Mapper and Reducer (word as Text)
        job.setOutputKeyClass(Text.class);
        // Specify the output value class for the Mapper and Reducer (count as IntWritable)
        job.setOutputValueClass(IntWritable.class);

        // Set the input path for the MapReduce job (the first command-line argument)
        FileInputFormat.addInputPath(job, new Path(args[0]));
        // Set the output path for the MapReduce job (the second command-line argument)
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // Submit the MapReduce job and wait for its completion (true parameter)
        // If the job is successful, exit with status 0; otherwise, exit with status 1
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
