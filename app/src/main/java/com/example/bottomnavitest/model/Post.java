package com.example.bottomnavitest.model;

import java.util.Date;

import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class Post {
    private String title;
    private String subject;
    private Date createdDate;
    private int commentNum;
    private long viewCount;
    private long userId;
    public Post(long userId, String title, String subject){
        this.userId = userId;
        this.title = title;
        this.subject = subject;
        this.commentNum = 0;
        this.viewCount = 0;
        this.createdDate = getCreatedDate();
    }

}
