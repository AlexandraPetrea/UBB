package Model;

public class BibliographyEntry {

    private Integer id;
    private String author;
    private String title;
    private String text;
    private Integer votes;

    public BibliographyEntry(Integer id, String author, String title, String text, Integer votes) {
        this.id = id;
        this.author = author;
        this.title = title;
        this.text = text;
        this.votes = 0;
    }

    public BibliographyEntry(String author, String title, String text, Integer votes) {
        this.author = author;
        this.title = title;
        this.text = text;
        this.votes = votes;
    }

    public Integer getId() {
        return id;
    }

    public Integer getVotes() {
        return votes;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public String getText() {
        return text;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setText(String text) {
        this.text = text;
    }

    public void setVotes(Integer votes) {
        this.votes = votes;
    }

    public void vote(){
        this.votes = votes + 1;
    }

}
