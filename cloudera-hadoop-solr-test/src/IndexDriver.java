import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class IndexDriver extends Configured implements Tool {     

  public static void main(String[] args) throws Exception {
    //TODO: Add some checks here to validate the input path
    int exitCode = ToolRunner.run(new Configuration(),
     new IndexDriver(), args);
    System.exit(exitCode);
  }

  
  public int run(String[] args) throws Exception {
    JobConf conf = new JobConf(getConf(), IndexDriver.class);
    conf.setJobName("Index Builder - Adam S @ Cloudera");
    conf.setSpeculativeExecution(false);

    // Set Input and Output paths
    FileInputFormat.setInputPaths(conf, new Path(args[0].toString()));
    FileOutputFormat.setOutputPath(conf, new Path(args[1].toString()));
    // Use TextInputFormat
    conf.setInputFormat(TextInputFormat.class);

    // Mapper has no output
    conf.setMapperClass(IndexMapper.class);
    conf.setMapOutputKeyClass(NullWritable.class);
    conf.setMapOutputValueClass(NullWritable.class);
    conf.setNumReduceTasks(0);
    JobClient.runJob(conf);
    return 0;
  }
}