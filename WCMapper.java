package wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class WCMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    // Declare a constant IntWritable with value 1 to be used as the output value for each word occurrence
    private final static IntWritable one = new IntWritable(1);
    // Declare a Text variable to store the word to be emitted as the output key
    private Text word = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        // Convert the input value (a line of text) to a String
        String line = value.toString();
        // Split the line into individual words using whitespace as the delimiter
        String[] parts = line.split("\\s+");
        // Loop through each word in the line
        for (String term : parts) {
            // Set the word as the current term to be emitted as the output key
            word.set(term);
            // Emit the word and its count (one occurrence) as the output (key-value pair)
            context.write(word, one);
        }
    }
}
