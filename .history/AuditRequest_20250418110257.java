import java.util.List;

/**
 * 审核请求对象
 */
public class AuditRequest {
    
    /**
     * 追踪ID
     */
    private String traceId;
    
    /**
     * 组ID
     */
    private Long groupId;
    
    /**
     * ID列表
     */
    private List<Long> ids;
    
    /**
     * 备注
     */
    private String remark;
    
    /**
     * 来源
     */
    private Integer source;
    
    /**
     * 操作人
     */
    private String operator;
    
    /**
     * 是否通过
     */
    private Boolean pass;

    // Getters and Setters
    public String getTraceId() {
        return traceId;
    }

    public void setTraceId(String traceId) {
        this.traceId = traceId;
    }

    public Long getGroupId() {
        return groupId;
    }

    public void setGroupId(Long groupId) {
        this.groupId = groupId;
    }

    public List<Long> getIds() {
        return ids;
    }

    public void setIds(List<Long> ids) {
        this.ids = ids;
    }

    public String getRemark() {
        return remark;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }

    public Integer getSource() {
        return source;
    }

    public void setSource(Integer source) {
        this.source = source;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public Boolean getPass() {
        return pass;
    }

    public void setPass(Boolean pass) {
        this.pass = pass;
    }

    @Override
    public String toString() {
        return "AuditRequest{" +
                "traceId='" + traceId + '\'' +
                ", groupId=" + groupId +
                ", ids=" + ids +
                ", remark='" + remark + '\'' +
                ", source=" + source +
                ", operator='" + operator + '\'' +
                ", pass=" + pass +
                '}';
    }
} 