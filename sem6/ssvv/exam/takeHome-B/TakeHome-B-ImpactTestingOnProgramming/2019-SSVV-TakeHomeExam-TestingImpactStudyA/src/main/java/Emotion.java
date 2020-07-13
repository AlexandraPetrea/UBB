import java.util.Objects;

public class Emotion {

    private String description;

    private EmotionType emotionType;

    public Emotion(String d, EmotionType et){
        this.description = d;
        this.emotionType = et;
    }
    public String getDesc() {
        return description;
    }

    public void setDesc(String d) {
        this.description = d;
    }
    public EmotionType getEmotionType() {
        return emotionType;
    }

    public void EmotionType(EmotionType et) {
        this.emotionType = et;
    }

    public String toString() {
        return "Emotion: " + emotionType +". Description:"+ description;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Emotion emotion = (Emotion) o;
        return Objects.equals(description, emotion.description) &&
                emotionType == emotion.emotionType;
    }

    @Override
    public int hashCode() {
        return Objects.hash(description, emotionType);
    }

}
