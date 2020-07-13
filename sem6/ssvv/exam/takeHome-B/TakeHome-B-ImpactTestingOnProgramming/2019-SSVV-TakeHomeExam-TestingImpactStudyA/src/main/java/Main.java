import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main (String[] args) {
        List lEmotions = new ArrayList<Emotion>();

        ListEmotions le = new ListEmotions(lEmotions);

        System.out.println(String.valueOf(le.howGivenManyEmotionTypeInListEmotions(EmotionType.Joy)));

        Emotion eJ = new Emotion("Joy", EmotionType.Joy);
        lEmotions.add(eJ);
        Emotion eS = new Emotion("Sadness", EmotionType.Sadness);
        lEmotions.add(eS);
        Emotion eD = new Emotion("Disgust", EmotionType.Disgust);
        lEmotions.add(eD);
        Emotion eD1 = new Emotion("Fear", EmotionType.Fear);
        lEmotions.add(eD1);


        System.out.println(String.valueOf(le.howGivenManyEmotionTypeInListEmotions(EmotionType.Joy)));

        Emotion eA = new Emotion("Joy", EmotionType.Joy);
        lEmotions.add(eA);
        Emotion eF = new Emotion("Fear", EmotionType.Fear);
        lEmotions.add(eF);

        System.out.println(String.valueOf(le.howGivenManyEmotionTypeInListEmotions(EmotionType.Joy)));
    }
}
