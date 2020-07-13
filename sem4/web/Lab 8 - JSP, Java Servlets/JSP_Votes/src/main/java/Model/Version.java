package Model;

import java.sql.Date;
import java.sql.SQLData;

public class Version {

    private Integer idversion;
    private Integer idobject;
    private Integer iduser;
    private String content;
    private Date date;

    public Version(Integer idobject, Integer iduser, String content) {

        this.idobject = idobject;
        this.iduser = iduser;
        this.content = content;


    }

    public Version(Integer idobject, Integer iduser, String content, Date date) {

        this.idobject = idobject;
        this.iduser = iduser;
        this.content = content;
        this.date = date;

    }

    public Version(Integer idversion, Integer idobject, Integer iduser, String content, Date date) {
        this.idversion = idversion;
        this.idobject = idobject;
        this.iduser = iduser;
        this.content = content;
        this.date = date;
    }

    public void setIdversion(Integer idversion) {
        this.idversion = idversion;
    }

    public void setIdobject(Integer idobject) {
        this.idobject = idobject;
    }

    public void setIduser(Integer iduser) {
        this.iduser = iduser;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Integer getIdversion() {
        return idversion;
    }

    public Integer getIdobject() {
        return idobject;
    }

    public Integer getIduser() {
        return iduser;
    }

    public String getContent() {
        return content;
    }

    public Date getDate() {
        return date;
    }
}

