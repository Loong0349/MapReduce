package wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class WCReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    // Declare an IntWritable variable to store the final count for each word
    private IntWritable result = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        // Initialize a variable to hold the sum of counts for the current word
        int sum = 0;
        // Loop through the values (counts) associated with the current word (key)
        for (IntWritable value : values) {
            // Add the current value (count) to the sum
            sum += value.get();
        }
        // Set the final count (sum) for the current word
        result.set(sum);
        // Emit the word and its final count as the output (key-value pair)
        context.write(key, result);
    }
}
